FROM alpine:edge

RUN apk add bash
RUN apk add john
RUN apk add wireshark
RUN apk add tshark
RUN apk add termshark


