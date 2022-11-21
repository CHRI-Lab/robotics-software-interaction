# 7. SLAM


## building a spatio-temporal memory for the robot

Probablilistic robotics

- localisation with landmarks
- localisation with edges


Uncertainty 
- measurement errors (sensors are not accurate)
- actuation errors (actions never do excactly wht they are supposed to)

## conditional probablility and bayes rule

P(E|O) = probablity that E is true given that we observe O

P(cold|cough) = P(cold) * P(cough|cold)
i.e. . if we know the prior probability that I have a
cold (without any evidence) and I know that a cold
causes a cough, with some probability, then we
can calculate the posterior probability

### probablilistic inference

Bayes rule: P(H|E) = P(H) x P(E|H)

or bel(x_t) = bel(x_t-1) x prob(observation)


## Updating State Estimate - Kalman filter
• The Kalman filter is commonly used to update the estimate of the robot’s
state
• Two phases:
1. Prediction (Process Update)
• predicts where the robot will be after performing an action
2. Correction (Observation Update)
• use observations to correct prediction
• What follows is only a sketch of the Kalman filter
• It’s nowhere near the complete algorithm