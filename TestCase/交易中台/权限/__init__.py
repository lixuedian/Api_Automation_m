from Config.Config import Config

config = Config()
url = config.test_mp_url
url = '%s%s' % ('http://', url)
header = {
    'Content-Type': 'application/json',
    'token': config.token_zt
}
