#!/usr/bin/env ruby

def greeting
    popcorn = Time.now
    puts 'Hello, World!  Today is ' + popcorn.strftime("%Y-%m-%d")
end

greeting
