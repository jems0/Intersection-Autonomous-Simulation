% Define the initial positions and velocities of the dots
pos1 = [-5 0]; % starting position of dot 1 (on the left side of the plot)
pos2 = [0 -5]; % starting position of dot 2 (in the middle of the y-axis)
vel1 = [0.3 0]; % velocity vector for dot 1 (moves right horizontally)
vel2_orig = [0 0.3]; % original velocity vector for dot 2 (moves up vertically)
vel2 = vel2_orig; % current velocity vector for dot 2 (initially set to original velocity)

% Set up the figure
fig = figure;
axis([-10 10 -10 10]);
hold on;

% Game Theory Values
alpha = 0.5;
beta = 1 - alpha;

% Plot the initial positions of the dots
h1 = plot(pos1(1), pos1(2), 'bo', 'MarkerFaceColor', 'blue');
h2 = plot(pos2(1), pos2(2), 'ro', 'MarkerFaceColor', 'red');

% Move the dots
for t = 1:100
    % Update the position of dot 1
    pos1 = pos1 + vel1;
    
    % Update the position of dot 2 using game theory
    % Calculate the distance and relative velocity between the dots
    dist = norm(pos1 - pos2);
    rel_vel = vel1 - vel2;
    
    % Calculate the optimal velocity for dot 2
    if dist < 1 % if the dots are too close
        vel2 = beta * vel2 + alpha * (pos2 - pos1) / (dist^2); % move away from dot 1
    else % if the dots are far enough apart
        vel2 = vel2_orig; % resume original velocity
    end
    
    % Check if the dots intersect
    if dist <= 1
        % Stop dot 2
        vel2 = [0 0];
        pos2 = pos2 + vel2; % don't move dot 2 backwards
    else
        pos2 = pos2 + vel2; % update the position of dot 2
    end
    
    % Update the plot
    set(h1, 'XData', pos1(1), 'YData', pos1(2));
    set(h2, 'XData', pos2(1), 'YData', pos2(2));
    pause(0.1);
end
