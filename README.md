# devops-netology
Зайцев Алексей

будут игнорироваться следующие файлы ( в масках * = любой символ) 
1. все файлы в каталогах ".terraform" не зависимо от их глубины расположения от корня 
2. все файлы по маске "*.tfstate" и "* .tfstate.*"
3. Игнорировать файл crash.log в текущем каталоге
4. игнорировать все файлы с расширением *.tfvars
5. игнрировать файлы : override.tf, overridetf.json, и по маске *_override.tf, *_override.tf.json
6. игнорировать файлы по маске *.terraformrc и terraform.rc
---in new brannch
