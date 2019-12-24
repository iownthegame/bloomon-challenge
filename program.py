class BouquetDesign:
    def __init__(self, bouquet_design_string):

        # process bouquet_design_string
        self.name = bouquet_design_string[0]
        self.size = bouquet_design_string[1]

        num = -1
        flowers = {}
        for i in range(2, len(bouquet_design_string)):
            c = bouquet_design_string[i]
            if not c.isdigit():
                flowers[c] = num
                num = -1
            else:
                if num == -1:
                    num = int(c)
                else:
                    num = num * 10 + int(c)

        self.needed_flowers = flowers
        self.prepared_flowers = {}
        self.total_quantities = num

    def add_prepared_flowers(self, flower):
        if flower.size != self.size:
            return
        if not flower.name in self.prepared_flowers:
            self.prepared_flowers[flower.name] = [flower.idx]
        else:
            self.prepared_flowers[flower.name] += [flower.idx]

    def remove_prepared_flowers(self, consumed_flowers):
        for key, idx_list in consumed_flowers.items():
            if key in self.prepared_flowers:
                for idx in idx_list:
                    try:
                        self.prepared_flowers[key].remove(idx)
                    except ValueError:
                        pass

    def produce(self):
        for key, value in self.needed_flowers.items():
            if not key in self.prepared_flowers:
                return None
            if not len(self.prepared_flowers[key]) >= value:
                return None

        consumed_flowers = {}
        candidates = []
        remain_num = self.total_quantities - sum(list(self.needed_flowers.values()))
        for key, idx_list in self.prepared_flowers.items():
            if key in self.needed_flowers:
                value = self.needed_flowers[key]
                consumed_flowers[key] = idx_list[:value]
                for i in range(value, len(idx_list)):
                    candidates.append([idx_list[i], key])
            else:
                for idx in idx_list:
                    candidates.append([idx, key])

        if remain_num == 0:
            return consumed_flowers

        if len(candidates) < remain_num:
            return None

        candidates.sort(key=lambda x: x[0])
        for i in range(remain_num):
            idx, key = candidates[i]
            if key in consumed_flowers:
                consumed_flowers[key] += [idx]
            else:
                consumed_flowers[key] = [idx]
        return consumed_flowers

    def get_bouquet(self, consumed_flowers):
        flower_list = sorted(consumed_flowers.keys())
        flowers_output = ''.join([f'{len(consumed_flowers[key])}{key}' for key in flower_list])
        output = f'{self.name}{self.size}{flowers_output}'
        return output

    def __repr__(self):
        flower_list = sorted(self.needed_flowers.keys())
        flowers_output = ''.join([f'{self.needed_flowers[key]}{key}' for key in flower_list])
        output = f'{self.name}{self.size}{flowers_output}{self.total_quantities}'
        return output

class Flower:
    def __init__(self, name, size, idx):
        self.name = name
        self.size = size
        self.idx = idx

    def __repr__(self):
        return f'{self.name}{self.size}'

class InputStream:
    def __init__(self):
        pass

    def get_input(self):
        line = input()
        return line.strip()

class OutputStream:
    def __init__(self):
        pass

    def write(self, output):
        print(output)

class Application:
    def __init__(self):
        self.bouquetDesigns = []
        self.parseFlower = False
        self.flowers = {}
        self.idx = 0

    def process(self, string):
        bouquet = None
        if not self.parseFlower:
            if not string:
                self.parseFlower = True
            else:
                bouquetDesign = BouquetDesign(string)
                self.bouquetDesigns.append(bouquetDesign)
        else:
            # add flower into prepared_flowers
            flower = Flower(string[0], string[1], self.idx)
            self.idx += 1
            for bouquetDesign in self.bouquetDesigns:
                bouquetDesign.add_prepared_flowers(flower)

            # test to produce one bouquet
            producedBouquetDesign = None
            for bouquetDesign in self.bouquetDesigns:
                consumed_flowers = bouquetDesign.produce()
                if consumed_flowers:
                    producedBouquetDesign = bouquetDesign
                    break

            # remove flowers in prepared_flowers which has been comsumed
            if producedBouquetDesign:
                bouquet = producedBouquetDesign.get_bouquet(consumed_flowers)

                for bouquetDesign in self.bouquetDesigns:
                    bouquetDesign.remove_prepared_flowers(consumed_flowers)

        return bouquet

def run():
    # input
    """
    bouquet design1
    bouquet design2
    <empty line>
    flower1
    flower2
    flower3
    """

    # output
    """
    bouquet1
    bouquet2
    """

    app = Application()
    inputStream = InputStream()
    outputStream = OutputStream()

    while True:
        input_string = inputStream.get_input()
        output = app.process(input_string)
        if output:
            outputStream.write(output)

if __name__ == '__main__':
    run()
