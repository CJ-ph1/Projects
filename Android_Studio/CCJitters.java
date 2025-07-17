package com.mendez.compilationactivity;

import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.CompoundButton;
import android.widget.RadioButton;
import android.widget.TextView;

import java.util.Locale;

public class CCJitters extends AppCompatActivity {

    // Constants for item prices
    private static final double CAFFE_VANILLA_FRAPPUCCINO_PRICE = 150.00;
    private static final double GREEN_TEA_CREME_FRAPPUCCINO_PRICE = 190.00;
    private static final double SMORES_FRAPPUCCINO_PRICE = 199.00;
    private static final double MOCHA_FRAPPUCCINO_PRICE = 130.00;

    // UI elements
    private CheckBox checkBox1, checkBox2, checkBox3, checkBox4;
    private RadioButton radioButton1, radioButton2, radioButton3, radioButton4;
    private TextView subtotalTextView, discountTextView, netAmountTextView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.ccjitters_main);

        // Initialize UI elements
        checkBox1 = findViewById(R.id.checkBox);
        checkBox2 = findViewById(R.id.checkBox2);
        checkBox3 = findViewById(R.id.checkBox3);
        checkBox4 = findViewById(R.id.checkBox4);

        radioButton1 = findViewById(R.id.radioButton);
        radioButton2 = findViewById(R.id.radioButton2);
        radioButton3 = findViewById(R.id.radioButton3);
        radioButton4 = findViewById(R.id.radioButton4);

        subtotalTextView = findViewById(R.id.textView10);
        discountTextView = findViewById(R.id.textView11);
        netAmountTextView = findViewById(R.id.textView12);

        Button computeButton = findViewById(R.id.button);
        Button clearAllButton = findViewById(R.id.button2);

        // Set onClickListener for Compute button
        computeButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                compute();
            }
        });

        // Set onClickListener for Clear All button
        clearAllButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                clearAll();
            }
        });

        // Set listener for Discount radio buttons
        CompoundButton.OnCheckedChangeListener discountListener = new CompoundButton.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
                if (isChecked) {
                    clearDiscountRadioButtons(buttonView.getId());
                }
            }
        };

        radioButton1.setOnCheckedChangeListener(discountListener);
        radioButton2.setOnCheckedChangeListener(discountListener);
        radioButton3.setOnCheckedChangeListener(discountListener);
        radioButton4.setOnCheckedChangeListener(discountListener);

        // Compute initially
        compute();
    }

    // Compute function to calculate subtotal, discount, and net amount
    private void compute() {
        double subtotal = 0;
        double discount = 0;

        if (checkBox1.isChecked()) subtotal += CAFFE_VANILLA_FRAPPUCCINO_PRICE;
        if (checkBox2.isChecked()) subtotal += GREEN_TEA_CREME_FRAPPUCCINO_PRICE;
        if (checkBox3.isChecked()) subtotal += SMORES_FRAPPUCCINO_PRICE;
        if (checkBox4.isChecked()) subtotal += MOCHA_FRAPPUCCINO_PRICE;

        // Apply discount
        if (radioButton1.isChecked()) discount = subtotal * 0.05;
        else if (radioButton2.isChecked()) discount = subtotal * 0.10;
        else if (radioButton3.isChecked()) discount = subtotal * 0.15;

        double netAmount = subtotal - discount;

        // Update TextViews
        subtotalTextView.setText(String.format(Locale.getDefault(), "$%.2f", subtotal));
        discountTextView.setText(String.format(Locale.getDefault(), "$%.2f", discount));
        netAmountTextView.setText(String.format(Locale.getDefault(), "$%.2f", netAmount));
    }

    // Clear All function to reset UI
    private void clearAll() {
        // Deselect all checkboxes
        checkBox1.setChecked(false);
        checkBox2.setChecked(false);
        checkBox3.setChecked(false);
        checkBox4.setChecked(false);

        // Leave the "No Discount" radio button checked
        radioButton4.setChecked(true);

        // Clear other discount radio buttons
        clearDiscountRadioButtons(radioButton4.getId());

        // Reset TextViews
        subtotalTextView.setText("$0.00");
        discountTextView.setText("$0.00");
        netAmountTextView.setText("$0.00");
    }

    // Clear discount radio buttons except the one specified by the given id
    private void clearDiscountRadioButtons(int idToKeep) {
        if (radioButton1.getId() != idToKeep) radioButton1.setChecked(false);
        if (radioButton2.getId() != idToKeep) radioButton2.setChecked(false);
        if (radioButton3.getId() != idToKeep) radioButton3.setChecked(false);
        if (radioButton4.getId() != idToKeep) radioButton4.setChecked(false);
    }
}