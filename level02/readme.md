ls -la
I found a file level02.pcap (whireshark)
scp -P 4242 level02@192.168.1.39:/home/user/level02/level02.pcap . (to download file in local machine)
work with the level02.pcap file in whireshark
I fonund in data de word "passwrd"
shark -Tfields -e data.data -r level02.pcap | tr -d "\n" | xxd -r -p
