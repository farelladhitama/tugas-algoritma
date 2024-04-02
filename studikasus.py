def pesan_usia(usia):
    if usia < 18:
        print("Hiduplah dengan semangat belajar dan jelajahi dunia di sekitarmu dengan rasa ingin tahu yang besar!")
    elif 18 <= usia < 60:
        print("Manfaatkan waktu Anda untuk mengejar impian dan mencapai tujuan Anda.")
    else:
        print("Nikmati setiap momen hidup dan manfaatkan pengalaman Anda untuk memberikan inspirasi kepada generasi mendatang.")

usia = int(input("Berapa usia Anda? "))
pesan_usia(usia)