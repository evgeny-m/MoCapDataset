import sys
import os
import pickle

dataset_part = "Parts1_and_2"
dataset_split = "3/5"

if __name__ == "__main__":    

    if (len(sys.argv) > 1):
        dataset_part = sys.argv[1]
        
    if (dataset_part == "Part1"):
        parts_info = [ ("Part1", "gest") ]
        cls_map = {1:0, 2:1, 3:2, 4:3, 5:4, 6:5, 7:6, 8:7, 9:8,  10:9}
    elif (dataset_part == "Part2"):
        parts_info = [ ("Part2", "ctrl") ]
        cls_map = {11:0, 12:1, 13:2, 14:3, 15:4, 16:5, 17:6, 18:7, 19:8, 20:9, 21:10, 22:11, 23:12, 24:13, 25:14, 26:15, 27:16, 28:17}
    elif (dataset_part == "Parts1_and_2"):
        parts_info = [ ("Part1", "gest"), ("Part2", "ctrl") ]
        cls_map = {1:0, 2:1, 3:2, 4:3, 5:4, 6:5, 7:6, 8:7, 9:8,  10:9, 11:10, 12:11, 13:12, 14:13, 15:14, 16:15, 17:16, 18:17, 19:18, 20:19, 21:20, 22:21, 23:22, 24:23, 25:24, 26:25, 27:26, 28:27}
    elif (dataset_part == "Part3"):
        parts_info = [ ("Part3", "inst") ]
        cls_map = {1:0, 2:1, 3:1, 4:2, 5:2, 6:4, 7:3, 8:4, 9:4,  10:5, 11:6, 12:6, 13:7, 14:8, 15:9, 16:10}
        #cls_map = {1:0, 2:1, 3:2, 4:3, 5:4, 6:5, 7:6, 8:7, 9:8,  10:9, 11:10, 12:11, 13:12, 14:13, 15:14, 16:15}
    elif (sys.argv[1] == "Part4"):
        cls_map = {1:0, 2:1, 3:2, 4:3, 5:4, 6:5, 7:6, 8:7, 9:8,  10:9, 11:10, 12:11, 13:12, 14:13, 15:14, 16:15, 17:16, 18:17, 19:18, 20:19, 21:20, 22:21, 23:22, 24:23, 25:24, 26:25}
        parts_info = [ ("Part4", "evrd") ]
    else: 
        print("Unknown dataset: ", sys.argv[1])
        exit()
    
    # read files
    xs = [];  # sequences
    ys = [];  # classes
    ps = [];  # actors (persons)
    es = [];  # attempt numbers
    for person in [1,2,3,4]:
        for att_no in range(1,6):
            for cls in cls_map:
                for (part, prefix) in parts_info:
                    pkl_path = "%s%02d_%02d_%02d.pkl" % (prefix, person, att_no, cls)
                    pkl_path = os.path.join("..", part, pkl_path)
                    if os.path.isfile( pkl_path ):
                        print("read file: ", pkl_path);
                        with open(pkl_path, 'rb') as h:
                            data = pickle.load(h);
                        xs.append( data[0][0] );  
                        ys.append( cls_map[cls] );
                        ps.append( person );
                        es.append( att_no );
                            
    print("\ntotal ", len(xs), " sequences in ", dataset_part);    
    
    
    # train/test split
    if (dataset_split == "2/5"): # two fifth for training
        train_idxs = [i for i in range(len(es)) if es[i] in [2,4]];
        test_idxs  = [i for i in range(len(es)) if es[i] in [1,3,5]];
    elif (dataset_split == "3/5"): # three fifth for training
        train_idxs = [i for i in range(len(es)) if es[i] in [1,3,5]];
        test_idxs  = [i for i in range(len(es)) if es[i] in [2,4]];
    elif (dataset_split == "4/5"): # four fifth for training
        train_idxs = [i for i in range(len(es)) if es[i] != 3];
        test_idxs  = [i for i in range(len(es)) if es[i] == 3];
    else: # cross subject
        print("Unknown split: ", split);
        exit();
        
    x_train = [xs[i] for i in train_idxs];
    y_train = [ys[i] for i in train_idxs];
    x_test  = [xs[i] for i in test_idxs ];
    y_test  = [ys[i] for i in test_idxs ];
    
    
    # some numbers
    print("number of train sequences: ", len(train_idxs))
    print("number of test  sequences: ", len(test_idxs))
    print("ratio: ", len(train_idxs)/len(test_idxs))
    
    lengths = [len(x) for x in x_train];
    print("train sequence lengths: ", min(lengths), "...", max(lengths));
    lengths = [len(x) for x in x_test];
    print("test sequence lengths: ", min(lengths), "...", max(lengths));
    
    print("pose dimensionality: ", len(x_train[0][0]));
    
    cls_set = set(y_train + y_test)
    print("number of classes: ", len(cls_set))
    print("classes: ", cls_set)