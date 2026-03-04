# Radio Arbitration

## Goal
Share a single SX1262 radio between Meshtastic mesh traffic and LoRaWAN uplinks without collisions, while keeping power use predictable and within regional duty-cycle limits.

## Superframe schedule (baseline)
- Superframe length: 60 seconds.
- Guard time between slots: 150 ms.
- Meshtastic RX windows: 4 windows per superframe, each 1.5 seconds.
- Meshtastic TX budget: 2 bursts per superframe, each up to 400 ms.
- LoRaWAN TX window: 1 window per superframe, up to 400 ms.

### Slot map (example)
1) RX_MESH_1 (1.5s)  
2) RX_MESH_2 (1.5s)  
3) TX_MESH_1 (0.4s)  
4) RX_MESH_3 (1.5s)  
5) RX_MESH_4 (1.5s)  
6) TX_LORAWAN_1 (0.4s)  
7) TX_MESH_2 (0.4s)  

Guard time is applied before every slot to allow radio retune and MCU wake.

## Arbitration policy
- **Idle mode**: Follow baseline superframe (approx 80/20 mesh/LoRaWAN time budget).
- **Meet mode**: Preempt all LoRaWAN TX; mesh RX/TX only (100/0).
- **Active mode**: Increase LoRaWAN TX window to 2 per superframe (50/50).
- **Emergency uplink**: Allow a single LoRaWAN TX preemption if the queue age exceeds 10 minutes.

## Backoff and retries
- Mesh TX: exponential backoff with jitter (base 250 ms, max 4 seconds).
- LoRaWAN TX: use stack backoff; schedule next try into the next available LoRa slot.
- If both queues are non-empty, prioritize:
  1) Meet/Whitelist messages
  2) Safety alerts
  3) Status updates

## Duty-cycle compliance
- Track total TX airtime per hour and enforce region limits (e.g., 1%).
- If budget exceeded, defer non-critical TX to the next hour window.

## Observability
- Log slot utilization, preemptions, and drops into the event log.
- Provide a debug counter set for testing (mesh_tx, mesh_rx, lorawan_tx, preemptions).
