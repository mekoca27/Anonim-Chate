# Anonim-Chate
• GhostLink: Universal Terminal Chat System
GhostLink, Python Socket mimarisi kullanılarak geliştirilmiş; Windows, Linux ve Termux platformları arasında köprü kuran, hafif ve gerçek zamanlı bir mesajlaşma protokolüdür.
✨ Öne Çıkan Özellikler
📱 Platform Özgürlüğü: Özel geliştirilmiş istemciler (clients) sayesinde Termux, Windows CMD ve Linux Terminal üzerinde %100 uyumlu renk ve ekran yönetimi.
🛡️ Soket Kararlılığı: Soket hatalarına (BrokenPipe, ConnectionReset) karşı güçlendirilmiş, bağlantı kopsa dahi ana sistemi çökertmeyen mimari.
🔑 Dinamik Oda Sistemi: Rastgele üretilen 6 haneli oda ID'leri ile anlık gizli odalar oluşturma.
💾 Kalıcı Ayarlar: settings.json ile kullanıcı adınız otomatik olarak kaydedilir.
🎨 Estetik Arayüz: Gri saat damgası, sarı ayraç ve mesaj iletimini doğrulayan yeşil yıldız (*) desteği.
🎮 Komut Listesi
Sohbet ekranındayken aşağıdaki komutları metin satırına yazarak kullanabilirsiniz:
create-room:limit -> Belirlediğiniz kişi kapasitesine sahip yeni bir oda açar ve size özel bir ID verir. (Örn: create-room:5)
join ID -> Arkadaşınızın oluşturduğu 6 haneli odaya katılmanızı sağlar. (Örn: join AB12CD)
config-name:yeni_isim -> Kullanıcı adınızı anlık olarak günceller ve hafızaya kaydeder.
close-room -> (Sadece Admin) Bulunduğunuz odayı tamamen kapatır.
exit -> Sunucu bağlantısını güvenli bir şekilde keserek uygulamadan çıkar.
🛠️ Kurulum ve Çalıştırma
1. Sunucu (Server) Kurulumu
Sunucu kodunu bir hosting veya uzak sunucuda (VDS) çalıştırın:
python server.py
2. İstemci (Client) Kurulumu
Cihazınıza uygun olan dosyayı terminal üzerinden çalıştırın:
Termux / Pydroid3 için: python termux_client.py
Windows (CMD/PowerShell) için: python win_client.py
Linux (Bash) için: python linux_client.py
📝 Mesaj Formatı
Sohbet akışı terminalinizde şu estetik yapıda görünür:
[22:15 10/02] | KullanıcıAdı: Mesaj metni buraya gelir *
⚙️ Teknik Detaylar
Dil: Python 3.x
Protokol: TCP (Transmission Control Protocol)
Mimari: Çok iş parçacıklı (Multithreading) asenkron dinleme.
Karakter Seti: UTF-8 (Tam Türkçe desteği).
