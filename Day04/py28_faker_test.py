from faker import Faker
import pandas as pd

dummy = Faker()
print(dummy.name())

dummy1 = Faker('ko-KR')
print(dummy1.name())
print(dummy1.address())
print(dummy1.company())

dummy_data = [[dummy1.name(), dummy1.postcode(), dummy1.address(), dummy1.phone_number(), dummy1.email()] for i in range(1000)]
# print(dummy_data)

df = pd.DataFrame(data=dummy_data, columns=['이름', '우편번호', '주소', '전화번호', '이메일'])
df.to_csv('./Day04/dummy_members2.csv', index=True, encoding='utf-8')
print('CSV 파일 생성 완료')