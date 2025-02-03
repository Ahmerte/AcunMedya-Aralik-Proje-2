# Kullanıcıdan notları alma
vize = float(input("Vize notunu gir: "))
final = float(input("Final notunu gir: "))

# Not ağırlıkları
vize_oran = 0.4
final_oran = 0.6

# Ortalama hesaplama
ortalama = (vize * vize_oran) + (final * final_oran)

# Geçti/Kaldı kontrolü
if final < 50:
    print(f"Ortalaman: {ortalama:.2f} - Finalin 50’nin altında olduğu için kaldın!")
elif ortalama >= 50:
    print(f"Ortalaman: {ortalama:.2f} - Tebrikler, geçtin!")
else:
    print(f"Ortalaman: {ortalama:.2f} - Maalesef, kaldın.")
