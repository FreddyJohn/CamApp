import boto3
import os

class s3logic:

    def __init__(self,bucketname):
        self.s3client=boto3.client('s3')
        self.bucketname=bucketname

    def downloadFileGiven(self,objectkey):
        
        filename=os.path.join('tmp',objectkey.replace("/",""))
        self.s3client.download_file(self.bucketname,objectkey,filename)
        return filename

    def getDirectoryPrefixesGiven(self,prefix,delimeter):
        directorycontent=[]
        response=self.s3client.list_objects(Bucket=self.bucketname,Prefix=prefix,Delimiter=delimeter)
        if prefix.count('/')==4:
            delimeter=''
            for objectkey in response['Contents']:
                directorycontent.append(objectkey['Key'])
            return directorycontent
        else:
            for paritalprefix in response['CommonPrefixes']:
                directorycontent.append([paritalprefix['Prefix']])
            return directorycontent

