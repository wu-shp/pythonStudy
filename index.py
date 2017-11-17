number = [];
for value in range(1,18):
    numbers = value ** 2;
    number.append(numbers);
    print(number);
dimensions = (200,50);
print(dimensions[0]);
print(dimensions[1]);
for dimension in dimensions:
    print(dimension);
cars = ['audi','bmw','subaru','toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
car = 'bmw'
car == 'bmw';
sdsd = 'mudsud'
if sdsd != 'sdas':
    print("sadsd")
age = 18;
age == 18;
alien_0 = {'color':'green','points':5}
print(alien_0['color'])
print(alien_0['points'])
user_0 = {
    'username':'efermi',
    'first':'enrico',
    'last':'fermi',
}
for key,value in user_0.items():
    print("\nKey:"+key)
    print("Value:"+value)
favorite_languages = {
    'jen':'python',
    'sarah':'ruby',
    'edward':'c'
}
for name in favorite_languages.keys():
    print(name.title())
wsd = input("说出你的名字：")
print(wsd);
prompt =  "你好啊"
prompt += "\n具体?"
name = input(prompt)
print("/我说,"+name+"!")
age = input("你多大")
height = input("how tall are you,in inches?")
height = int(height);
if height >= 23:
    print("\nyou are tall enough to ride!")
else:
    print("\nyou will be able to ride when you are a littl older")

x =1;
while x <= 5:
    print(x)

a = ['alice','branch','candace']
b = []
while a:
    d = a.pop()
    print("Verifying user:"+d.title())
    b.append(d)
print("\nThe following users have been confirmed:")
for c in b:
    print(b.title())

