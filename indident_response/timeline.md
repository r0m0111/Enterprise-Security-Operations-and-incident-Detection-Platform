# Incident 001 Timeline
- ex
| Time | Event | Source | Significance |
|------|-------|--------|--------------|
| 18:01 | Failed SSH login | auth.log | Authentication failure |
| 18:01 | Failed SSH login | auth.log | Repeated failure |
| 18:02 | Failed SSH login | auth.log | Repeated failure |
| 18:02 | Failed SSH login | auth.log | Repeated failure |
| 18:03 | Failed SSH login | auth.log | Brute-force threshold |
| 18:03 | Successful SSH login | auth.log | Potential compromise |
| 18:04 | GET /admin | Nginx | Suspicious web request |
| 18:04 | GET /.env | Nginx | Suspicious web request |
