# Исследование абсолютной погрешности метода численного дифференцирования

В данном проекте прдеставлена возможность исследования абсолютной погрешности метода численного дифференцирования в зависимости от шага $h_n = {2 \over 2^n}$ для $n=1..21$ <br/>
По оси x представлен $\ln(n)$, а по $y$ $\ln(|f'(x) - g(x)|)$, где $g(x)$ -  функция численного дифференцирования

## Выполнение

Функции, которые мы будем исследовать:
-    $\sin(x^2)$
-    $\cos(\sin(x))$
-    $\exp(\sin(\cos(x)))$
-    $\ln(x+3)$
-    $\sqrt{x+3}$

А также сами функции численного дифференцирования: 

+ ${f(x + h) - f(x) \over h}$
+ ${f(x) - f(x - h) \over h}$
+ ${f(x + h) - f(x - h) \over 2 * h}$
+ ${4 \over 3} {f(x + h) - f(x - h) \over 2 * h} - {1 \over 3} {f(x + 2h) - f(x - 2h) \over 4h}$
+ ${3 \over 2} {f(x + h) - f(x - h) \over 2 * h} - {3 \over 5} {f(x + 2h) - f(x - 2h) \over 4h} + {1 \over 10} {f(x + 3h) - f(x - 3h) \over 6h}$

Первые две функции при разложении в ряд Тейлора дают остаток $(O(h))$, когда начиная с третьей порядок начинает увеличиваться на единицу, то есть $(O(h^n))$
Посмотрим на получившиеся графики для данных функций
<div class="img-div">
  <img src="https://github.com/EnikAs/Computational-Mathematics/blob/main/1Task/%D0%93%D1%80%D0%B0%D1%84%D0%B8%D0%BA%20%D0%B4%D0%BB%D1%8F%20%D1%84%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D0%B8%20sin(x%5E2).png" width="450" alt="">
  <img src="https://github.com/EnikAs/Computational-Mathematics/blob/main/1Task/%D0%93%D1%80%D0%B0%D1%84%D0%B8%D0%BA%20%D0%B4%D0%BB%D1%8F%20%D1%84%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D0%B8%20cos(sin(x)).png" width="450" alt="">
  <img src="https://github.com/EnikAs/Computational-Mathematics/blob/main/1Task/%D0%93%D1%80%D0%B0%D1%84%D0%B8%D0%BA%20%D0%B4%D0%BB%D1%8F%20%D1%84%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D0%B8%20exp(sin(cos(x))).png" width="450" alt="">
  <img src="https://github.com/EnikAs/Computational-Mathematics/blob/main/1Task/%D0%93%D1%80%D0%B0%D1%84%D0%B8%D0%BA%20%D0%B4%D0%BB%D1%8F%20%D1%84%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D0%B8%20ln(x%2B3).png" width="450" alt="">
  <img src="https://github.com/EnikAs/Computational-Mathematics/blob/main/1Task/%D0%93%D1%80%D0%B0%D1%84%D0%B8%D0%BA%20%D0%B4%D0%BB%D1%8F%20%D1%84%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D0%B8%20(x%2B3)%5E0%2C5.png" width="450" alt="">
</div>
