echo "=== EXECUTANDO COMANDOS ==="
echo "Data antes:  $(date)"
yum update tzdata -y
rm -rf /root/localtime.old
mv /etc/localtime /root/localtime.old
ln -s /usr/share/zoneinfo/America/Bahia /etc/localtime
hwclock -w
echo "Data depois: $(date)"
echo " "
