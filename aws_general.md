### AWS CLI & Environment Variable
#### References
* https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-envvars.html

```
gedit ~/.aws/config 
gedit ~/.aws/credentials
aws configure
```
### CodeCommit
#### References
* https://docs.aws.amazon.com/codecommit/latest/userguide/getting-started-cc.html
```
git config --global credential.helper '!aws codecommit credential-helper $@'
git config --global credential.UseHttpPath true
git clone "repo"
```

