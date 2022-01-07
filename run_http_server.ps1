echo "run this as admin!!"
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
http-server -p 1111 -c-1 "C:/Users/sdlyn/Repositories/screen_lights/public"
