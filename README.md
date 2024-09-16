# 108trigo

Further exploration of matrix operations using fundamental functions.

Project for semester 2 of the Epitech Math module.

### Description

This program computes the result of applying a trigonometric or hyperbolic function to a matrix. Functions like exponentiation, cosine, sine, and hyperbolic sine are applied to matrices, expanding their power series representation. The matrix is provided as arguments, and the program computes the result using the chosen function.

### Functions supported:
- **EXP**: Exponential function
- **COS**: Cosine function
- **SIN**: Sine function
- **COSH**: Hyperbolic cosine
- **SINH**: Hyperbolic sine

Matrix-managing libraries are not allowed, so all matrix manipulations must be coded manually.

## Getting Started

### Dependencies

- [Python3](https://python.org/)

### Installation

* Download/Clone the repository and enter its directory.
* You are now ready to run the code.

## Usage

**Execution:** ```./108trigo fun a0 a1 a2 ...```

### Arguments
- **`fun`**: The function to apply. Options: "EXP", "COS", "SIN", "COSH", "SINH".
- **`ai`**: The coefficients of the matrix, passed in row-major order.

### Examples

To compute the cosine of a 3x3 matrix:

```
$> ./108trigo COS 4 5 9 3 3 5 0 1 9
0.70 -0.43 -1.94
-0.16 0.67 -1.23
-0.06 -0.15 0.07
```

To compute the exponential of a 2x2 matrix:

```
$> ./108trigo EXP 1 2 3 4
51.97 74.74
112.10 164.07
```

To compute the hyperbolic sine of a matrix:

```
$> ./108trigo SINH 1 0 2 0
1.18 0.00
2.35 0.00
```

## Acknowledgments

* [Epitech](https://www.epitech.eu/)

## Authors

* **Daniel Sanchez** ([GitHub](https://github.com/angsanch) / [LinkedIn](https://www.linkedin.com/in/angeldanielsanchez/))
* **Xinru Xu** ([GitHub](https://github.com/Exinru) / [LinkedIn](https://www.linkedin.com/in/xinru-xu/))

## License

This project is licensed under the GNU Public License version 3.0 - see the [LICENSE](LICENSE) file for details.
