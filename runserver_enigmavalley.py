import sys
import os.path

sys.path.append('../veil')
import veil.cli.testing



if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append('chazelle')
    import vendor
    vendor.vendorify()

    sys.argv = ['./bin/veil-test-server', '-L', 'debug', '-P', '3002',
                '--secret-key', 'plain', 'radically ephemeral flimsy kumquats',
                '--vhost-path', 'enigmavalley',
                'test.json',
                os.path.abspath('./assets/')]
    veil.cli.testing.run_server()
