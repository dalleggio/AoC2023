#!/usr/bin/env python
# coding: utf-8

from pprint import pprint

def run_wf(wf, wf_step, data):
    for datum in data:
        exec(datum)
    wf_list = wf[wf_step].split(',')
    for step in wf_list:
        if ':' in step:
            cond, next_wf = step.split(':')
            if eval(cond):
                return next_wf
            else:
                continue
    return step

def sum_cats(data):
    for datum in data:
        exec(datum)
    sum = 0
    for cat in ('x', 'm', 'a', 's'):
        sum += locals()[cat]
    return sum

fn = "data/workflows.txt"

wf = {}
with open(fn) as fin:
    for line in fin:
        if line.strip() != '':
            wf_kv = line.strip().split('{')
            wf[wf_kv[0]] = wf_kv[1][:-1]
        else:
            break
            
    #pprint(wf)
    ##print()
    sum_a = 0
    for line in fin:
        if line.strip() != '':
            data = line.strip()[1:-1].split(',')
            #print('data: ', data)
            wf_step = 'in'
            while wf_step not in ('A', 'R'):
                wf_step = run_wf(wf, wf_step, data)
                #print ('wf step: ', wf_step)
                if wf_step == 'A':
                    sum_a += sum_cats(data)
    print('sum: ', sum_a)