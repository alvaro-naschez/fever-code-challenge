# Fever Code Challenge

Read the original [instructions](instructions.md) of the challenge.

***

## Requirements
- [Docker Compose](https://docs.docker.com/compose/)
- [GNU Make](https://www.gnu.org/software/make/)

## How to run the solution
```sh
make run
```

> **WARNING**:
> What this does under the hood is just to execute `docker compose up`, so if you're using the legacy `docker-compose` CLI instead of `docker compose`, you will have to run `docker-compose up` instead.

> **Note**
> I'm using [GNU Make](https://www.gnu.org/software/make/) here because I was asked to do so in the instructions of the challenge, but for local development I've been using [Taskfile](https://taskfile.dev/) instead, which is a similar but more modern tool. I would recomend you to have a look to its documentation if you have some time.

## Goals of the proposed solution
My aim with the proposed solution was to find the right balance between a good and correct solution in one hand, and a simple one in the other. In other words I wanted to make things simple while not doing the bare minimum.

## Proposed architecture
The idea of the solution is really simple. We have a Postgres cluster with two replicas, a master replica and a slave replica. The idea is that we are going to be reading from the slave and writing to the master. So the updates we do in the data don't slow down the response time of our API endpoint.

> **Note**
> While I was implementing the solution I've found an event which comes with date of September 31st, which is obviously wrong because there are only 30 days in September. What I'm doing in that scenario is just to log the error and ignore the event.

> **Note**
> The `id` of the events in the feed is an `integer`, while in the OpenAPI spec the `id` of the events is of type `UUID`. I could have created an artificial UUID in my local DB, but I've decided not to do so and to use the ingeger `id` in the API output too. So that's the only little thing I've changed in the API spec. As I said I could have respected the instructions 100% here (it is not hard to do it) but I thought it makes no sense and my solution could be a lot cleaner this way.

## Closing thoughts
Obviously the app is not production ready. But I honestly believe I've done a good job given the time constraints.

In case you have any doubts about my solution, I would like to tell you that I would be more than happy to explain you my solution in more depth and why I made the decisions I made. So if you feel it could be useful, don't hesitate to organize a meeting in order to do so.

And finally I will explain why I don't have tests. I'm a bit ashamed that I don't have here a good test coverage. But writting good tests takes time. And I've currently spent some time in this challenge, I think it is enough at least for now. If some of these days I have time and I'm in the right mood I will write some.
