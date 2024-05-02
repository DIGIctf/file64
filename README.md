# file64
file64 will convert any file to a base64 string and save that to a .file64 extension. You can give this .file64 out to others and instead of transferring the file directly to them, they can recreate that file instantly on their own machine. This was created for educational purposes for ethical hacking.

This can be useful in the following situations:
<ul>
<li>-Spotty / terrible internet connection</li>
<li>-No internet connection at all</li>
<li>-Undetected</li>
</ul>
<h2>Install</h2>
```
git clone https://github.com/DIGIctf/file64.git
```


<h3>Sender:</h3>
```
$ python3 file64_encode.py <input_file>
$ python3 file64_encode.py testing.zip
```
This will create the base64 encryption of the zip file and save it to a special format, testing.zip.file64. You can send this file to others or display on a website and others can create the file on their own system. 

<h3>Receiver:</h3>
```
$ python3 file64_decode.py <file64_encoded_file>
$ python3 file64_decode.py testing.zip.file64
```
This will create a file, testing.zip. 

The md5sum of testing.zip and testing_decoded.zip are the same. 


