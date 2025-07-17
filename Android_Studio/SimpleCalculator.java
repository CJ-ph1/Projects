package com.mendez.compilationactivity;

import android.graphics.Color;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import androidx.appcompat.app.AppCompatActivity;

public class SimpleCalculator extends AppCompatActivity {

    EditText etFirstNumber, etSecondNumber;
    Button btnAdd, btnDiff, btnProd, btnQuo;
    TextView tvResultSum, tvResultProd, tvResult;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.simplecalculator_main);

        etFirstNumber = findViewById(R.id.etFirstNumber);
        etSecondNumber = findViewById(R.id.etSecondNumber);
        btnAdd = findViewById(R.id.btnAdd);
        btnDiff = findViewById(R.id.btnDiff);
        btnProd = findViewById(R.id.btnProd);
        btnQuo = findViewById(R.id.btnQuo);
        tvResultSum = findViewById(R.id.tvResultSum);
        tvResultProd = findViewById(R.id.tvResultProd);
        tvResult = findViewById(R.id.tvResult);

        btnAdd.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                calculateResult('+', "total sum:");
            }
        });

        btnDiff.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                calculateResult('-', "total sub:");
            }
        });

        btnProd.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                calculateResult('*', "total prod:");
            }
        });

        btnQuo.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                calculateResult('/', "total div:");
            }
        });
    }

    private void calculateResult(char operation, String resultText) {
        double num1 = Double.parseDouble(etFirstNumber.getText().toString());
        double num2 = Double.parseDouble(etSecondNumber.getText().toString());
        double result = 0;

        switch (operation) {
            case '+':
                result = num1 + num2;
                break;
            case '-':
                result = num1 - num2;
                break;
            case '*':
                result = num1 * num2;
                break;
            case '/':
                if (num2 != 0)
                    result = num1 / num2;
                else
                    tvResultSum.setText("Cannot divide by zero");
                break;
        }

        // Set text color based on result being odd or even
        int color = (result % 2 == 0) ? Color.BLUE : Color.RED;

        tvResultSum.setText(resultText + " " + result);
        tvResultSum.setTextColor(color);
    }
}
