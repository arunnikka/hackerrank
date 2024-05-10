Mahasiswa = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
nilai = [siswa[1] for siswa in Mahasiswa]
nilai_unik= sorted(set(nilai))
nilai_rendah_kedua = nilai_unik[1]
nilai_mahasiswa_terendah = [student[0] for student in Mahasiswa if student[1] == nilai_rendah_kedua]
nilai_mahasiswa_terendah.sort()
for student in nilai_mahasiswa_terendah:
        print(student)

