mkdir /var/www/llm;
chown -R www-data:www-data /var/www/llm;
rsync -rv frontend/dist/* /var/www/llm/

sudo useradd -r -s /bin/false llmagent
mkdir /opt/llm-agent
cd backend 
bash install
cd ..
rsync -rv baclend/agent.py /opt/llm-agent/
rsync -rv baclend/run.sh /opt/llm-agent/
rsync -rv baclend/app.py /opt/llm-agent/
rsync -rv baclend/venv /opt/llm-agent/

sudo chown -R llmagent:llmagent /opt/llm-agent
sudo chmod -R 755 /opt/llm-agent

cp service/llm-agent.service /etc/systemd/system/llm-agent.service

sudo systemctl daemon-reload
sudo systemctl enable llm-agent
sudo systemctl start llm-agent

cd backend
bash install.sh

sudo apt update
sudo apt install nginx

cp nginx/llm.config /etc/nginx/sites-available/llm-agent
sudo ln -s /etc/nginx/sites-available/llm-agent /etc/nginx/sites-enabled/
sudo rm /etc/nginx/sites-enabled/default

sudo nginx -t
sudo systemctl reload nginx

sudo certbot --nginx -d llm.strangebit.io
