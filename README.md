# fitbit

## Run locally
1. Export your Fitbit data, move your `Takeout` directory into the project directory.
2. Create an `.env` file (copy-paste from `.env.template`).
3. Run Docker + MySQL server using the `./setup.sh` script from `spotify-playback-poller` project.
4. To process the Fitbit data and insert it into the database, run:
```sh
./main.py userId fitbitDirectory
# for example: ./main.py 001 ./Takeout/Fitbit
```