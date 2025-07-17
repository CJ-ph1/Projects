package com.mendez.compilationactivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

public class PayrollSummary extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_payroll_summary);

        // Retrieve data from Intent
        Bundle extras = getIntent().getExtras();
        String employeeId = extras.getString("employeeId");
        String employeeName = extras.getString("employeeName");
        String positionCode = extras.getString("positionCode");
        String daysWorked = extras.getString("daysWorked");
        String civilStatus = extras.getString("civilStatus");
        double basicPay = extras.getDouble("basicPay");
        double sssContribution = extras.getDouble("sssContribution");
        double withholdingTax = extras.getDouble("withholdingTax");
        double netPay = extras.getDouble("netPay");

        // Display data in TextViews
        TextView employeeIdTextView = findViewById(R.id.textView19);
        TextView employeeNameTextView = findViewById(R.id.textView20);
        TextView positionCodeTextView = findViewById(R.id.textView21);
        TextView daysWorkedTextView = findViewById(R.id.textView24);
        TextView civilStatusTextView = findViewById(R.id.textView22);
        TextView basicPayTextView = findViewById(R.id.textView25);
        TextView sssContributionTextView = findViewById(R.id.textView26);
        TextView withholdingTaxTextView = findViewById(R.id.textView23);
        TextView netPayTextView = findViewById(R.id.textView27);

        employeeIdTextView.setText(employeeId);
        employeeNameTextView.setText(employeeName);
        positionCodeTextView.setText(positionCode);
        daysWorkedTextView.setText(daysWorked);
        civilStatusTextView.setText(civilStatus);
        basicPayTextView.setText(String.format("%.2f", basicPay));
        sssContributionTextView.setText(String.format("%.2f", sssContribution));
        withholdingTaxTextView.setText(String.format("%.2f", withholdingTax));
        netPayTextView.setText(String.format("%.2f", netPay));

        // Get the BACK button
        Button backButton = findViewById(R.id.button3);

        // Set OnClickListener for the BACK button
        backButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Finish the activity and return to MainActivity
                finish();
            }
        });
    }
}