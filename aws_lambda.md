### References
* https://docs.aws.amazon.com/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html

#### Without any Library Dependencies
```
1. Create Lambda Function in aws
2. zip function.zip function.py 
3. aws lambda update-function-code --function-name [I]function name [/I]--zip-file fileb://function.zip

```
#### With Library Dependencies
```
1.sudo pip3 install -t ~/....path to folder.../package numpy --ignore-installed
2.cd package
3.zip function.zip *
4.zip -g function.zip function.py
5.aws lambda update-function-code --function-name [I]function name [/I]--zip-file fileb://function.zip
```

#### Using VirtualEnv
```
1.source v-env/bin/activate
2.pip install XYZ
3.deactivate
4.cd v-env/lib/python3.7/site-packages 
5.zip function.zip *
6.zip -g function.zip function.py
7.aws lambda update-function-code --function-name [I]function name [/I]--zip-file fileb://function.zip
```
