
# frp

```
git clone https://github.com/daocodedao/voice-clone.git
```


```
cat /data/work/frp/frpc.ini 
vim /data/work/frp/frpc.ini

[ssh-voiceclone6251]
type = tcp
local_ip = 127.0.0.1
local_port = 9651
remote_port = 6251
use_encryption = false
use_compression = false



# 重启frp
sudo systemctl restart  supervisor
sudo supervisorctl reload
sudo supervisord
```