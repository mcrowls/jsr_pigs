% returns the days until target weight is found (instead of weight after x number of days)
function t = inverse_gombertz_matlab(target_weight, growth_rate)
    t = (1/growth_rate) * (log(log(target_weight)) - log(log(135)) + log(30));
end