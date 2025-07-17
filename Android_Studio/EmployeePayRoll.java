package com.mendez.compilationactivity;

import android.content.Intent;
import android.widget.Toast;
import android.os.Bundle;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.RadioButton;
import android.widget.RadioGroup;
import android.widget.Spinner;

import androidx.appcompat.app.AppCompatActivity;

public class EmployeePayRoll extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.employee_payroll);

        // Initialize spinners
        Spinner employeeIdSpinner = findViewById(R.id.spinner);
        Spinner positionCodeSpinner = findViewById(R.id.spinner2);
        Spinner daysWorkedSpinner = findViewById(R.id.spinner3);

        // Create array adapters
        ArrayAdapter<CharSequence> employeeIdAdapter = ArrayAdapter.createFromResource(this,
                R.array.employee_id_array, android.R.layout.simple_spinner_item);
        ArrayAdapter<CharSequence> positionCodeAdapter = ArrayAdapter.createFromResource(this,
                R.array.position_code_array, android.R.layout.simple_spinner_item);
        ArrayAdapter<CharSequence> daysWorkedAdapter = ArrayAdapter.createFromResource(this,
                R.array.days_worked_array, android.R.layout.simple_spinner_item);

        // Set dropdown layout resource
        employeeIdAdapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        positionCodeAdapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        daysWorkedAdapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);

        // Set adapters
        employeeIdSpinner.setAdapter(employeeIdAdapter);
        positionCodeSpinner.setAdapter(positionCodeAdapter);
        daysWorkedSpinner.setAdapter(daysWorkedAdapter);

        // Set default selection for spinners
        employeeIdSpinner.setSelection(0);
        positionCodeSpinner.setSelection(0);
        daysWorkedSpinner.setSelection(0);

        // Set hint for spinners
        employeeIdSpinner.setPrompt("Select Employee ID");
        positionCodeSpinner.setPrompt("Select Position Code");
        daysWorkedSpinner.setPrompt("Select No. of Days Worked");

        // Get the employee name EditText
        EditText employeeNameEditText = findViewById(R.id.editTextTextPersonName);

        // Get the radio group
        RadioGroup civilStatusRadioGroup = findViewById(R.id.civil_status_radio_group);

        // Get the COMPUTE button
        Button computeButton = findViewById(R.id.button2);

        // Set OnClickListener for the COMPUTE button
        computeButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Get selected data
                String employeeId = employeeIdSpinner.getSelectedItem().toString();
                String employeeName = employeeNameEditText.getText().toString();
                String positionCode = positionCodeSpinner.getSelectedItem().toString();
                String daysWorked = daysWorkedSpinner.getSelectedItem().toString();

                // Get selected radio button text
                String civilStatus = "";
                int selectedRadioButtonId = civilStatusRadioGroup.getCheckedRadioButtonId();
                if (selectedRadioButtonId != -1) {
                    RadioButton selectedRadioButton = findViewById(selectedRadioButtonId);
                    civilStatus = selectedRadioButton.getText().toString();
                }

                // Check if any field is empty
                if (employeeName.isEmpty() || civilStatus.isEmpty()) {
                    // Display error message
                    Toast.makeText(EmployeePayRoll.this, "Please fill in all the fields", Toast.LENGTH_SHORT).show();
                    return; // Exit the onClick method early
                }

                // Compute payroll data and pass to PayrollSummaryActivity
                double ratePerDay;
                switch (positionCode) {
                    case "A":
                        ratePerDay = 500.00;
                        break;
                    case "B":
                        ratePerDay = 400.00;
                        break;
                    case "C":
                        ratePerDay = 300.00;
                        break;
                    default:
                        ratePerDay = 0.00; // default value if position code is not recognized
                }

                int numberOfDaysWorked = Integer.parseInt(daysWorked);
                double basicPay = numberOfDaysWorked * ratePerDay;

                double taxRate;
                switch (civilStatus) {
                    case "Single":
                        taxRate = 0.10;
                        break;
                    case "Married":
                    case "Widowed":
                        taxRate = 0.05;
                        break;
                    default:
                        taxRate = 0.0; // default value if civil status is not recognized
                }

                double withholdingTax = basicPay * taxRate;

                double sssRate;
                if (basicPay >= 10000) {
                    sssRate = 0.07;
                } else if (basicPay >= 5000) {
                    sssRate = 0.05;
                } else if (basicPay >= 1000) {
                    sssRate = 0.03;
                } else {
                    sssRate = 0.01;
                }

                double sssContribution = basicPay * sssRate;

                double netPay = basicPay - (sssContribution + withholdingTax);

                Intent intent = new Intent(EmployeePayRoll.this, PayrollSummary.class);
                intent.putExtra("employeeId", employeeId);
                intent.putExtra("employeeName", employeeName);
                intent.putExtra("positionCode", positionCode);
                intent.putExtra("daysWorked", daysWorked);
                intent.putExtra("civilStatus", civilStatus);
                intent.putExtra("basicPay", basicPay);
                intent.putExtra("sssContribution", sssContribution);
                intent.putExtra("withholdingTax", withholdingTax);
                intent.putExtra("netPay", netPay);

                startActivity(intent);
            }
        });

        // Get the CLEAR button
        Button clearButton = findViewById(R.id.button);

        // Set OnClickListener for the CLEAR button
        clearButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Clear all input fields
                employeeNameEditText.setText("");
                employeeIdSpinner.setAdapter(employeeIdAdapter);
                positionCodeSpinner.setAdapter(positionCodeAdapter);
                daysWorkedSpinner.setAdapter(daysWorkedAdapter);
                civilStatusRadioGroup.clearCheck();
            }
        });
    }}