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
pip3 install --install-option="--prefix=$PREFIX_PATH" package_name --ignore-installed
```
