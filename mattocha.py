import numpy as np
import sympy as sp

def read_matrix_from_file(filename):
    """파일에서 행렬을 읽어들이고 유효한 정수만 처리합니다."""
    with open(filename, 'r') as f:
        data = f.read().strip()
    rows = data.split("\n")
    matrix = []
    for row in rows:
        matrix.append([int(x.strip()) for x in row.split(',') if x.strip()])
    return np.array(matrix)

def characteristic_polynomial(matrix):
    """행렬의 특성 다항식을 sympy로 계산"""
    n = matrix.shape[0]
    t = sp.symbols('t')
    M = sp.Matrix(matrix)
    poly = (t * sp.eye(n) - M).det()
    return sp.Poly(poly, t)

def format_polynomial_2(poly):
    """계수와 지수를 올바르게 포맷팅하여 다항식 출력"""
    terms = []
    for (exp,), coeff in poly.terms():
        if coeff >= 0 and terms:
            terms.append(f"+{coeff}")
        else:
            terms.append(f"{coeff}")
        if exp > 0:
            terms[-1] += f"*t^{exp}"
    return ''.join(terms).replace('+-', '-')

if __name__ == "__main__":
    # input.txt로부터 행렬 읽기
    matrix = read_matrix_from_file('input.txt')

    # 특성 다항식 계산
    poly = characteristic_polynomial(matrix)

    # 특성 다항식을 원하는 형식으로 출력
    formatted_poly = format_polynomial_2(poly)
    print(formatted_poly)
