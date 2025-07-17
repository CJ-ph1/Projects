package com.mendez.compilationactivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.Spinner;
import android.widget.Toast;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    private Spinner spinner;
    private Button button;
    private String selectedActivity;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        spinner = findViewById(R.id.spinner);
        button = findViewById(R.id.button);

        // Create an ArrayAdapter using the string array and a default spinner layout
        ArrayAdapter<CharSequence> adapter = ArrayAdapter.createFromResource(this,
                R.array.activity_list, android.R.layout.simple_spinner_item);

        // Specify the layout to use when the list of choices appears
        adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);

        // Apply the adapter to the spinner
        spinner.setAdapter(adapter);

        // Set the listener for spinner item selection
        spinner.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener() {
            @Override
            public void onItemSelected(AdapterView<?> parentView, View selectedItemView, int position, long id) {
                selectedActivity = parentView.getItemAtPosition(position).toString();
            }

            @Override
            public void onNothingSelected(AdapterView<?> parentView) {
                selectedActivity = null;
            }
        });

        // Set the listener for the button click
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if ("Simple Calculator".equals(selectedActivity)) {
                    Intent intent = new Intent(MainActivity.this, SimpleCalculator.class);
                    startActivity(intent);
                } else if ("CC Jitters".equals(selectedActivity)) {
                    Intent intent = new Intent(MainActivity.this, CCJitters.class);
                    startActivity(intent);
                } else if ("Semestral Grade".equals(selectedActivity)) {
                    Intent intent = new Intent(MainActivity.this, SemestralGrade.class);
                    startActivity(intent);
                } else if ("Employee Payroll".equals(selectedActivity)) {
                    Intent intent = new Intent(MainActivity.this, EmployeePayRoll.class);
                    startActivity(intent);
                } else {
                    Toast.makeText(MainActivity.this, "Please select an activity", Toast.LENGTH_SHORT).show();
                }
            }
        });
    }
}