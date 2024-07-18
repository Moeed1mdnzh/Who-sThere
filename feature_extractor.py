import os
import json
import torch


class Extractor:
    def __init__(self, base_file):
        with open(base_file, "r") as handle:
            self.db = json.loads(handle.read())
            self.keys = list(map(int, list(self.db.keys())))
        self.features = None
        self.path = "images"

    def load(self):
        self.features = torch.load(os.sep.join(
            [self.path, f"{self.keys[0]}.pt"]))
        for key in self.keys[1:]:
            self.features = torch.concat([self.features,
                                          torch.load(os.sep.join([self.path,
                                                                  f"{key}.pt"]))
                                          ])

    def process(self, feat):
        dist = torch.cdist(feat, self.features, p=2)
        index = torch.argmin(dist[0]).detach().numpy()
        return self.db[str(index)]
