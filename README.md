## Nepali Datetime API

Public APIs to access Nepali Datetime (Bikram Sambat Date & Nepal Time) with custom formatting options. The project is
completely based on library [`nepali_datetime`](https://github.com/amitgaru2/nepali-datetime).

_The public access url for the API is http://nepali-datetime.amitgaru.me (which
might change in future)._

### Basic Usage

1. To get today's Bikram Sambat Date

   ```sh
   curl -X GET http://nepali-datetime.amitgaru.me/date
   ```

   Will return `json` in the format

   ```json
   { "data": "2077-06-26" }
   ```

   Response format can be changed by

   ```sh
   curl -X GET "http://nepali-datetime.amitgaru.me/date?format=%d-%B-%y"
   ```

   Will return `json` in the format

   ```json
   { "data": "26-Aswin-77" }
   ```

   **More about the formatting in the table described [here](https://amitgaru2.github.io/nepali-datetime/html/index.html#strftime-and-strptime-behavior).**

1. Similarly, to get today's Bikram Sambat Date & current Nepal Time

   ```sh
    curl -X GET http://nepali-datetime.amitgaru.me/datetime
   ```

   Will return `json` in the format

   ```json
   { "data": "2077-06-26 01:04:46.769648" }
   ```

   Formatting can be applied with same behavior as described above.
