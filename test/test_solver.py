import pytest
import cmath

from my_quadratic_solver.solver import solve

def complex_are_close(c1, c2, abs_tol=1e-9):
    """Перевіряє, чи два комплексних числа є близькими."""
    return abs(c1.real - c2.real) < abs_tol and abs(c1.imag - c2.imag) < abs_tol

def test_two_real_roots():
    result = solve(1, -3, 2)
    assert result['type'] == 'two_real'
    assert result['delta'] == 1.0
    assert 1.0 in result['roots']
    assert 2.0 in result['roots']
    assert len(result['roots']) == 2

def test_one_real_root():
    result = solve(1, -2, 1)
    assert result['type'] == 'one_real'
    assert result['delta'] == 0.0
    assert result['roots'] == [1.0]
    assert len(result['roots']) == 1

def test_two_complex_roots():
    result = solve(1, 0, 1)
    assert result['type'] == 'two_complex'
    assert result['delta'] == -4.0
    assert len(result['roots']) == 2
    root1, root2 = result['roots']
    assert (complex_are_close(root1, 0+1j) and complex_are_close(root2, 0-1j)) or \
           (complex_are_close(root1, 0-1j) and complex_are_close(root2, 0+1j))

def test_complex_roots_with_b():
    result = solve(1, 2, 5)
    assert result['type'] == 'two_complex'
    assert result['delta'] == -16.0
    assert len(result['roots']) == 2
    root1, root2 = result['roots']
    assert (complex_are_close(root1, -1+2j) and complex_are_close(root2, -1-2j)) or \
           (complex_are_close(root1, -1-2j) and complex_are_close(root2, -1+2j))


def test_not_quadratic():
    result = solve(0, 2, 4)
    assert result['type'] == 'not_quadratic'
    assert result['roots'] is None

def test_large_coefficients():
    result = solve(1e10, 2e10, 1e10)
    assert result['type'] == 'one_real'
    assert abs(result['roots'][0] - (-1.0)) < 1e-9 

def test_fractional_coefficients():
    result = solve(0.5, -1.5, 1) 
    assert result['type'] == 'two_real'
    assert 1.0 in result['roots']
    assert 2.0 in result['roots']
    
skibidiballs