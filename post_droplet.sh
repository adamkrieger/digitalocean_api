curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer $DO_TOKEN" \
	-d '{"name":"example.com","region":"nyc3","size":"512mb","image":"ubuntu-14-04-x64","ssh_keys":null,"backups":false,"ipv6":true,"user_data":null,"private_networking":null,"volumes": null,"tags":["web"]}' "https://api.digitalocean.com/v2/droplets"
