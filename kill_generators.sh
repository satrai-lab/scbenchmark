sudo pkill -9 python3
sudo pkill -f "/bin/bash ./0_all_in_one_create.sh"
sudo docker-compose -f docker-compose-troe.yml down
sudo docker-compose -f docker-compose-troe.yml rm -f
