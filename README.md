# Capstone-3-Purwadhika

**Context**

Asuransi perjalanan merupakan jenis perlindungan yang diberikan kepada individu selama mereka melakukan perjalanan, baik domestik maupun internasional. Beberapa negara bahkan mewajibkan para pelancong untuk memiliki asuransi perjalanan, seperti negara-negara di Eropa dan Amerika. Besaran premi asuransi tergantung pada jenis perlindungan yang diinginkan, durasi perjalanan, serta tujuan perjalanan tersebut.

Perusahaan yang bergerak di bidang asuransi perjalanan memiliki data historis yang sangat berharga, yang mencakup berbagai fitur terkait dengan perjalanan dan pemegang polis. Fitur-fitur ini termasuk nama agen, jenis agen, saluran distribusi, produk yang dibeli, karakteristik pemegang polis (seperti usia dan jenis kelamin), durasi perjalanan, tujuan perjalanan, dan status klaim. Dengan data yang cukup lengkap ini, perusahaan ingin meningkatkan efisiensi operasional dan mengurangi risiko finansial melalui prediksi klaim yang lebih akurat.

**Problem Statement :**

Perusahaan asuransi perjalanan menghadapi tantangan untuk memprediksi kemungkinan klaim yang diajukan oleh pemegang polis berdasarkan data historis yang ada. Dalam konteks ini, perusahaan ingin dapat memanfaatkan data yang tersedia untuk membangun model prediktif yang mampu mengidentifikasi dengan tepat apakah suatu polis asuransi akan mengajukan klaim atau tidak.

Tantangan utama:
Bagaimana kita dapat mengembangkan model yang tidak hanya akurat dalam memprediksi status klaim, tetapi juga memberikan wawasan berharga yang membantu perusahaan dalam mengelola risiko finansial, mengalokasikan sumber daya dengan lebih efisien, dan memberikan pengalaman pelanggan yang lebih baik?

**Goals :**

Tujuan utama dari proyek ini adalah mengembangkan model prediktif untuk memprediksi kemungkinan klaim asuransi perjalanan dengan akurat, sehingga perusahaan dapat mengalokasikan sumber daya secara lebih efisien dan mengurangi biaya operasional serta risiko finansial.

Model ini juga diharapkan dapat meningkatkan kepuasan pelanggan dengan memberikan layanan yang lebih cepat dan responsif, serta membantu perusahaan merancang produk asuransi yang lebih sesuai dengan kebutuhan pasar dan mengoptimalkan saluran distribusi.

Secara keseluruhan, tujuan dari model ini adalah untuk mendukung pengambilan keputusan berbasis data yang mendorong pertumbuhan bisnis yang berkelanjutan.

**Analytic Approach :**

Sebagai data scientist, langkah pertama adalah **data preprocessing**, yang mencakup pembersihan data dan pengkodean fitur kategorikal. Kemudian, dilakukan **exploratory data analysis (EDA)** untuk memahami hubungan antar variabel. Beberapa algoritma machine learning, seperti **logistic regression** dan **random forest**, akan digunakan untuk membangun model prediktif, yang dievaluasi dengan metrik **F2-Score**. Model terbaik kemudian diimplementasikan untuk memprediksi klaim dan mendukung keputusan dalam pengelolaan sumber daya
