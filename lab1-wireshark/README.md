# Lab 1: Wireshark Network Analysis

## Screenshots
- Part 1 (HTTP Filter): `⁠⁠⁠⁠HTTP.png`
- Part 2 (TCP Handshake): `TCP.png`

## Part 4: Analysis & Questions

### Table 1: Handshake Steps
| Step | Packet Type | Description |
| --- | --- | --- |
| 1 | SYN | Client sends a SYN packet to initiate connection |
| 2 | SYN-ACK | Server responds with SYN-ACK to acknowledge |
| 3 | ACK | Client sends ACK to finalize connection setup |

### Table 2: HTTP vs HTTPS
| Feature | HTTP | HTTPS |
| --- | --- | --- |
| Encryption | No Encryption (Plaintext) | Encrypted using TLS/SSL |
| Port | Port 80 | Port 443 |
| Security | Vulnerable to packet sniffing | Secure against eavesdropping |

