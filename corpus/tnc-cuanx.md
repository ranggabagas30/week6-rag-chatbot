**Syarat, Ketentuan & Kebijakan Privasi CUAN-X**

Dokumen ini adalah ampliﬁkasi dari kebijakan yang sudah ada. Semua pasal baru bersifat addendum/replace terhadap pasal terkait di Syarat & Ketentuan dan Kebijakan Privasi CuanX.

**1\. Prinsip Umum — Safety First, Compliance First**

1.1. Semua layanan CuanX wajib mematuhi seluruh peraturan nasional dan peraturan sektoral (OJK/BI/PPATK/ Kemenhub/Kominfo/PP terkait pajak dan perlindungan konsumen).  
1.2. Pengguna dan mitra (driver, merchant, penyedia jasa pihak ketiga) wajib tunduk pada ketentuan ini; kegagalan mematuhi \= dasar pemblokiran/penangguhan/penutupan akun dan tuntutan ganti rugi.  
1.3. Semua istilah kunci (User, Merchant, Driver, Payment Provider, Processor, Subprocessor) didefinisikan jelas di Glosarium (lampiran) untuk menghilangkan ambiguitas.

**2\. Pernyataan & Jaminan (Representations and Warranties)**

2.1. Pengguna menegaskan bahwa data yang diberikan akurat, sah, bukan hasil penipuan.  
2.2. Mitra/driver/merchant menjamin kepatuhan hukum (perizinan usaha, pajak, izin transportasi, izin komersial).  
2.3. CuanX menjamin upaya teknis dan administratif untuk melindungi data sesuai kebijakan ini, namun tidak memberikan jaminan absolut (lihat pembatasan tanggung jawab).

**3\. Batasan & Pembatasan Tanggung Jawab (Limitation of Liability)**

3.1. Batas tanggung jawab langsung CuanX terhadap klaim apa pun dibatasi hingga jumlah maksimal yang dibayar oleh pengguna kepada CuanX dalam 12 bulan terakhir sebelum klaim.  
3.2. CuanX tidak bertanggung jawab atas: (a) kerugian tidak langsung, insidentil, konsekuensial, punitive, kehilangan goodwill, kehilangan profit; (b) tindakan pihak ketiga termasuk merchant/airline/hotel; (c) gangguan layanan akibat force majeure.  
3.3. Tidak ada klaim yang bisa diajukan lebih dari jangka waktu 12 bulan sejak kejadian.

**4\. Indemnitas (Ganti Rugi)**

4.1. Pengguna, merchant, dan mitra wajib mengganti rugi (indemnify) CuanX atas semua klaim, biaya, kerugian, biaya hukum, denda regulator, yang timbul akibat: penyalahgunaan layanan, pelanggaran data oleh pihak mereka, pelanggaran pernyataan/jaminan, atau tindakan melanggar hukum.  
4.2. CuanX berhak menuntut ganti rugi dan/atau menahan dana akun hingga resolusi.

**5\. KYC, AML, & Keamanan Finansial (Fintech-specific)**

5.1. Semua pengguna yang menggunakan layanan fintech wajib melengkapi **KYC Level** sesuai risiko (basic, enhanced). KYC wajib sebelum akses fungsi tertentu (top-up besar, transfer ke bank, payout).  
5.2. CuanX berhak menahan/menolak transaksi yang terindikasi pencucian uang, pendanaan teroris, atau kegiatan ilegal, dan wajib melaporkan ke **PPATK**.  
5.3. Transaksi tertentu dikenai limit harian/bulanan; CuanX dapat mengubah limit tanpa pemberitahuan sebelumnya demi kepatuhan/regulator.  
5.4. Semua gateway/payment provider harus mematuhi PCI-DSS; data kartu tidak boleh tersimpan kecuali menggunakan tokenisasi yang disetujui.

**6\. Pengelolaan Insiden & Pelaporan Kebocoran Data (Breach Response)**

6.1. CuanX mengadopsi **Incident Response Plan**: deteksi → isolasi → mitigasi → forensik → notifikasi.  
6.2. Notifikasi internal regulator & pengguna: pemberitahuan awal kepada regulator lokal (Kominfo/PPATK/OJK bila relevan) dalam **72 jam** setelah deteksi material breach; pemberitahuan pengguna individual tanpa penundaan yang tidak perlu.  
6.3. Semua bukti forensik disimpan; CuanX berhak menunda permintaan penghapusan sementara untuk keperluan penyelidikan kriminal atau penegakan hukum.

**7\. Data Minimization, Retention & Deletion**

7.1. Prinsip minimisasi: hanya simpan data yang diperlukan untuk tujuan bisnis dan kewajiban hukum.  
7.2. Retensi default:

* Catatan transaksi keuangan: **5 tahun** (atau sesuai peraturan pajak/fintech).  
* Data operasional ride (ruta, log): **1–3 tahun** tergantung kepentingan keselamatan/forensik.  
* Data pengguna non-aktif: dianonimkan setelah 12 bulan tidak aktif, kecuali kewajiban hukum.  
  7.3. Permintaan deletion: verifikasi identitas ketat; penolakan bila ada kewajiban hukum atau sengketa. Semua permintaan di-log dan bisa diuji audit.

**8\. Penggunaan Audio/Video dalam Kendaraan**

8.1. Rekaman audio/video boleh dilakukan hanya untuk tujuan keselamatan dan bukti sengketa; pengguna diinformasikan secara jelas (consent pop-up) dan periode retensi singkat (mis. 30–90 hari).  
8.2. Akses rekaman hanya untuk pihak berwenang, fungsi internal keselamatan, atau atas perintah pengadilan. Mitra driver dilarang menyebarkan rekaman.

**9\. Subprocessors, Vendor & Third-Party Risk**

9.1. Semua vendor pihak ketiga (hosting, payment, telemetry, SMS) wajib tandatangan **Data Processing Agreement (DPA)** yang memuat: pembatasan pemanfaatan data, kewajiban keamanan, sub-processing chain disclosure, dan audit rights.  
9.2. CuanX wajib mempublikasikan daftar sub-processor utama dan memberikan pemberitahuan 30 hari sebelum perubahan material.  
9.3. Hak audit: CuanX dan/atau auditor independen berhak audit kepatuhan vendor (setiap 12 bulan atau atas insiden).

**10\. Keamanan Teknis & Operational Controls**

10.1. Standar wajib: ISO 27001, PCI-DSS (untuk payment), OWASP top 10 mitigations, SOC2 Type II audit (disarankan).  
10.2. Enkripsi: data at-rest & in-transit wajib AES-256/TLS1.2+.  
10.3. Akses: least-privilege & MFA untuk admin. Logging immutable & retention log minimal 1 tahun.  
10.4. Testing: pentest triwulan, scanning kerentanan mingguan, bug bounty program dengan kebijakan pembayaran & triage.

**11\. Pembayaran, Escrow & Settlement Rules (Fintech & OTA)**

11.1. Dana pengguna yang belum disalurkan (escrow) harus dipisahkan dari akun operasional perusahaan dan dicatat sesuai peraturan dompet elektronik.  
11.2. Penyelesaian klaim/chargeback: prosedur dispute resolution 30 hari; CuanX dapat menahan dana sampai penyelesaian.  
11.3. Merchant refund SLA ditetapkan (mis. refund OTA 7–14 hari) dan merchant bertanggung jawab atas data yang salah.

**12\. Penangguhan & Pemutusan Layanan**

12.1. CuanX berhak menangguhkan/menutup akun tanpa pemberitahuan jika ditemukan: pelanggaran hukum, aktivitas fraud, ancaman keamanan, atau perintah regulator.  
12.2. Saat penangguhan, data dibekukan; akses restorasi tergantung hasil investigasi.  
12.3. Pengguna berhak banding melalui mekanisme internal (Customer Escalation Mechanism) dalam jangka waktu 14 hari setelah penangguhan.

**13\. Force Majeure & Keadaan Darurat**

13.1. Peristiwa di luar kendali (bencana, pemutusan infrastruktur, keputusan regulator, perang, pandemi) membebaskan CuanX dari kewajiban temporal; pemberitahuan akan diberikan segera.  
13.2. Namun CuanX wajib mengambil langkah wajar untuk mengurangi dampak dan memberi kompensasi sesuai kebijakan (mis. voucher).

**14\. Kepatuhan Sektor Spesifik (Ringkasan Ketat)**

14.1. Ride-hailing: semua driver terdaftar, background check periodik (criminal record & driving license), kewajiban asuransi untuk penumpang.  
14.2. Fintech: lisensi/partnership dengan pihak berlisensi; pelaporan transaksi mencurigakan; limit KYC; penyimpanan bukti transaksi.  
14.3. Produk Digital: SLA supply, garansi top-up, proteksi terhadap fraud top-up.  
14.4. OTA: ketentuan pemesanan, cancel/refund policy yang jelas, tanggung jawab atas kesalahan data pihak ketiga.

**15\. Penyelesaian Sengketa & Pilihan Forum**

15.1. Mekanisme: wajib mediasi internal → arbitrase (BANI/BAWAS) atau Arbitrase Nasional/Internasional (pilih satu dan disesuaikan) — pilih **arbitrase di Jakarta** dengan aturan yang ditentukan.  
15.2. Pembatasan class action: pengguna setuju menyelesaikan sengketa individual kecuali hukum memerintahkan sebaliknya.  
15.3. Pajak dan biaya litigasi ditanggung oleh pihak yang kalah.

**16\. Audit, Compliance & Review Berkala**

16.1. Program kepatuhan internal (Compliance Program) wajib: Chief Compliance Officer, pelaporan triwulan ke dewan, annual compliance report publik ringkasan.  
16.2. Audit eksternal minimal sekali per tahun untuk keamanan & kepatuhan finansial.

**17\. Perubahan Kebijakan & Notifikasi**

17.1. Perubahan signifikan membutuhkan pemberitahuan minimal **30 hari** sebelum berlaku untuk memberi waktu adaptasi, kecuali perubahan karena perintah regulator (efektif segera dan diinformasikan).  
17.2. Perubahan diberitahukan melalui aplikasi, email, dan/atau pop-up in-app; persetujuan pengguna dianggap otomatis jika pengguna terus menggunakan layanan setelah periode 30 hari kecuali pengguna menyatakan keberatan.

**18\. Ketentuan Umum Lainnya**

18.1. Severability: jika suatu klausul dianggap tidak sah, seluruh ketentuan lain tetap berlaku.  
18.2. Entire Agreement: Dokumen ini adalah keseluruhan perjanjian; semua komunikasi sebelumnya tidak mengikat kecuali diintegrasikan tertulis.  
18.3. Assignment: CuanX berhak mengalihkan hak dan kewajiban ke afiliasi setelah memberi pemberitahuan; pengguna tidak boleh mengalihkan tanpa persetujuan.

