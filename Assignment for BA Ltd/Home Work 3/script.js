function add() {
    var num1 = parseFloat(document.getElementById('num1').value);
    var num2 = parseFloat(document.getElementById('num2').value);
    document.getElementById('result').value = num1 + num2;
}

function subtract() {
    var num1 = parseFloat(document.getElementById('num1').value);
    var num2 = parseFloat(document.getElementById('num2').value);
    document.getElementById('result').value = num1 - num2;
}

function multiply() {
    var num1 = parseFloat(document.getElementById('num1').value);
    var num2 = parseFloat(document.getElementById('num2').value);
    document.getElementById('result').value = num1 * num2;
}

function divide() {
    var num1 = parseFloat(document.getElementById('num1').value);
    var num2 = parseFloat(document.getElementById('num2').value);
    if (num2 === 0) {
        document.getElementById('result').value = "Cannot divide by zero";
    } else {
        document.getElementById('result').value = num1 / num2;
    }
}

function reset() {
    document.getElementById('num1').value = '';
    document.getElementById('num2').value = '';
    document.getElementById('result').value = '';
}
