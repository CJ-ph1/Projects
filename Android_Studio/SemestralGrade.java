package com.mendez.compilationactivity;

import androidx.appcompat.app.AppCompatActivity;
import android.app.AlertDialog;
import android.content.DialogInterface;
import android.graphics.Color;
import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class SemestralGrade extends AppCompatActivity {
    // UI elements
    private EditText nameEditText, grade1EditText, grade2EditText, grade3EditText;
    private TextView nameTextView, totalGradeTextView, ptEquivalentTextView, remarksTextView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.semestralgrade_main);

        // Initialize UI elements
        nameEditText = findViewById(R.id.editTextPersonName);
        grade1EditText = findViewById(R.id.editTextNumber1);
        grade2EditText = findViewById(R.id.editTextNumber2);
        grade3EditText = findViewById(R.id.editTextNumber3);
        nameTextView = findViewById(R.id.textView11);
        totalGradeTextView = findViewById(R.id.textView12);
        ptEquivalentTextView = findViewById(R.id.textView13);
        remarksTextView = findViewById(R.id.textView15);

        Button computeButton = findViewById(R.id.button2);
        Button newEntryButton = findViewById(R.id.button);

        // Set onClickListener for Compute button
        computeButton.setOnClickListener(v -> showComputeConfirmationDialog());

        // Set onClickListener for New Entry button
        newEntryButton.setOnClickListener(v -> showNewEntryConfirmationDialog());
    }

    private void showComputeConfirmationDialog() {
        // Check if any of the required fields are empty
        if (isAnyFieldEmpty()) {
            showErrorMessage("Please fill in all fields before computing the grade.");
            return;
        }

        new AlertDialog.Builder(this)
                .setMessage("Do you want to compute the results?")
                .setPositiveButton("Yes", (dialog, which) -> computeGrade())
                .setNegativeButton("No", null)
                .show();
    }

    private void showNewEntryConfirmationDialog() {
        new AlertDialog.Builder(this)
                .setMessage("Do you want to clear all entries and results?")
                .setPositiveButton("Yes", (dialog, which) -> clearEntriesAndResults())
                .setNegativeButton("No", null)
                .show();
    }

    private void computeGrade() {
        String name = nameEditText.getText().toString();
        double grade1 = Double.parseDouble(grade1EditText.getText().toString());
        double grade2 = Double.parseDouble(grade2EditText.getText().toString());
        double grade3 = Double.parseDouble(grade3EditText.getText().toString());

        // Validate grades entered for each subject
        if (!isValidGrade(grade1) || !isValidGrade(grade2) || !isValidGrade(grade3)) {
            showErrorMessage("Input Grade from 1 to 3 should be more than 50 and less than 100.");
            return;
        }

        double totalGrade = (grade1 + grade2 + grade3) / 3.0;

        String remarks;
        double ptEquivalent;
        int color;

        // Determine remarks, ptEquivalent, and color based on totalGrade
        if (totalGrade == 100) {
            remarks = "PASSED";
            ptEquivalent = 1.00;
            color = Color.BLUE;
        } else if (totalGrade >= 95) {
            remarks = "PASSED";
            ptEquivalent = 1.50;
            color = Color.BLUE;
        } else if (totalGrade >= 90) {
            remarks = "PASSED";
            ptEquivalent = 2.00;
            color = Color.BLUE;
        } else if (totalGrade >= 85) {
            remarks = "PASSED";
            ptEquivalent = 2.50;
            color = Color.BLUE;
        } else if (totalGrade >= 80) {
            remarks = "PASSED";
            ptEquivalent = 3.00;
            color = Color.BLUE;
        } else if (totalGrade >= 75) {
            remarks = "PASSED";
            ptEquivalent = 3.50;
            color = Color.BLUE;
        } else {
            remarks = "FAILED";
            ptEquivalent = 5.00;
            color = Color.RED;
        }

        // Update TextViews with computed values
        nameTextView.setText(name);
        totalGradeTextView.setText(String.format("%.2f", totalGrade));
        ptEquivalentTextView.setText(String.format("%.2f", ptEquivalent));
        remarksTextView.setText(remarks);
        remarksTextView.setTextColor(color);
    }
    private boolean isValidGrade(double grade) {
        return grade >= 50 && grade <= 100;
    }

    private void clearEntriesAndResults() {
        nameEditText.getText().clear();
        grade1EditText.getText().clear();
        grade2EditText.getText().clear();
        grade3EditText.getText().clear();
        nameTextView.setText("");
        totalGradeTextView.setText("");
        ptEquivalentTextView.setText("");
        remarksTextView.setText("");
    }

    private boolean isAnyFieldEmpty() {
        String name = nameEditText.getText().toString();
        String grade1Text = grade1EditText.getText().toString();
        String grade2Text = grade2EditText.getText().toString();
        String grade3Text = grade3EditText.getText().toString();

        return name.isEmpty() || grade1Text.isEmpty() || grade2Text.isEmpty() || grade3Text.isEmpty();
    }

    private void showErrorMessage(String message) {
        new AlertDialog.Builder(this)
                .setMessage(message)
                .setPositiveButton("OK", null)
                .show();
    }
}

