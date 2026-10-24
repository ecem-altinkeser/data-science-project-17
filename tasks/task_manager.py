import numpy as np
import matplotlib.pyplot as plt

def five_number_summary(data: list) -> dict:
    """
    Min, Q1, Median, Q3, Max değerlerini içeren sözlük döndür.
    Output örneği: {'min': ..., 'Q1': ..., 'median': ..., 'Q3': ..., 'max': ...}
    """
    return {"min":min(data), "Q1":np.quantile(data, 0.25), "median": np.median(data), "Q3":np.quantile(data, 0.75), "max": max(data)}

def detect_outliers(data: list) -> list:
    """
    IQR metoduyla aykırı değerleri tespit et.
    Output: [list of outliers]
    """
    q1 = np.quantile(data, 0.25)
    q3 = np.quantile(data, 0.75)
    iqr = q3-q1
    lower = q1 - 1.5*iqr
    higher = q3 + 1.5*iqr
    data1 = np.array(data)
    return data1[(data1<lower) | (data1 > higher)]

def draw_boxplot(data: list) -> None:
    """
    Verinin boxplot'unu çiz.
    Output: matplotlib görseli
    """
    plt.boxplot(data)
    plt.show()

def draw_histogram(data: list, title: str = "Histogram") -> None:
    """
    Histogramı çiz.
    """
    plt.hist(data, bins=4)
    plt.show()

#Input: [1, 2, 3, 4, 100]
#Output: skewness değeri, > 0 ise sağa çarpık
def calculate_skewness(data: list) -> float:
    """
    Veri setinin skewness (çarpıklık) değerini hesapla.
    """
    return (3*(np.mean(data)-np.median(data)))/np.std(data)


#Input: [1, 2, 3, 4, 100]
#skewness değerini hesaplamalısın. bu değere göre 'left', 'right' veya 'symmetric' değerini döndür
def is_skewed(data: list) -> str:
    """
    Skewness değerine göre 'left', 'right' veya 'symmetric' döndür.
    """
    skewness = calculate_skewness(data)
    if round(skewness) > 0:
        return "right"
    elif round(skewness) < 0:
        return 'left'
    else:
        return 'symmetric'
    
def calculate_covariance(x: list, y: list) -> float:
    """
    İki veri seti arasındaki kovaryansı hesapla.
    """
    return np.cov(x,y)[0,1]


def calculate_correlation(x: list, y: list) -> float:
    """
    Pearson correlation coefficient hesapla.
    """
    return  np.corrcoef(x,y)[0,1]

def is_positive_correlation(x: list, y: list) -> bool:
    """
    Korelasyon pozitif mi kontrol et.
    """
    return calculate_correlation(x,y) > 0

def compare_variables(x: list, y: list) -> dict:
    """
    Hem kovaryans hem de korelasyonu döndür.
    Output: {'covariance': ..., 'correlation': ...}
    """
    return {'covariance': calculate_covariance(x,y), 'correlation': calculate_correlation(x,y)}