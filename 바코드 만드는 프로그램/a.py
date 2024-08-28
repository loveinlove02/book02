import barcode
from barcode.writer import ImageWriter

# ISBN 번호
isbn_number = "9791160505856"
# 9791160506822 9791160505856 9791186697726 9791187431169 

# ISBN 바코드 생성 (이미지 파일로 저장)
ean = barcode.get('isbn13', isbn_number, writer=ImageWriter())

# 바코드 이미지를 파일로 저장 (PNG 형식)
filename = ean.save("isbn_barcode")

print(f"ISBN 바코드 이미지가 '{filename}.png'로 저장되었습니다.")
