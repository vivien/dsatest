
import unittest

from squidsa.bench import bench

class TestPing(unittest.TestCase):


    def setUp(self):
        links = bench.links

        for i, l in enumerate(links, start=1):
            host_addr = "192.168.10.{}/24".format(str(i * 2))
            sut_addr = "192.168.10.{}/24".format(str(i * 2 + 1))

            l.host_if.addAddress(host_addr)
            l.sut_if.addAddress(sut_addr)


    def tearDown(self):
        links = bench.links

        for i, l in enumerate(links, start=1):
            host_addr = "192.168.10.{}/24".format(str(i * 2))
            sut_addr = "192.168.10.{}/24".format(str(i * 2 + 1))

            l.host_if.delAddress(host_addr)
            l.sut_if.delAddress(sut_addr)


    def test_ping(self):
        links = bench.links
        if len(links) == 0:
            self.skipTest("Empty link list")

        for i, link in enumerate(links, start=1):
            addr = "192.168.10.{}".format(str(i * 2 + 1))
            link.host_if.ping(addr, count=1, deadline=10)
