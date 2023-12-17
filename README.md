# Amazon web mağazasında çok satan ilk 100 kitabın yorumlarına ve özelliklerine bağlı olarak değerlendirme skorlarının belirlenmesi / tahmini
Veri Kaynağı: [https://www.kaggle.com/datasets/anshtanwar/top-200-trending-books-with-reviews]

Amazon kullanıcılarının kitapları değerlendirme sırasında 1-5 aralığında, manuel olarak bir değer belirtmelerine gerek kalmadan yaptıkları yorumları, yorum yaptıkları zamanı(yıl ve mevsim) ve satın aldıkları fiyatı dikkate alarak 1-5 aralığında otomatik değerleme yapan model tasarladım

model olarak AdaBoost Regressor, Decision Tree Regressor, SVR ve Random Forest Regressor modellerini,
metrik olarak mean squared error metriğini kullandım.


