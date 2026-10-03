# 02: Full-Stack & Core Systems Foundations

This module targets core technical grilling for Citi's SWE Apprenticeship across React.js, Python async backends, MongoDB document modeling, and AWS Serverless infrastructure.

---

## 1. React.js & Modern Frontend Architecture

### Virtual DOM & Fiber Reconciliation
1. **The Problem**: Manipulating the actual browser DOM is expensive because every change causes style recalculation, layout reflow, and repaint.
2. **Virtual DOM**: A lightweight JavaScript object tree mirroring the actual DOM.
3. **Reconciliation (React Fiber)**:
   * React calculates differences between old and new Fiber nodes using a heuristic $\mathcal{O}(N)$ algorithm based on two assumptions:
     * Two elements of different types produce completely different trees.
     * Elements with stable `key` props preserve identity across renders.
   * **Fiber Architecture**: Splits rendering work into incremental chunks. High-priority user interactions (typing, clicks) can interrupt low-priority background data rendering.

### Essential React Hooks & Traps
* `useEffect(fn, deps)`: Executes side-effects after layout paint. Missing dependencies cause stale closures; passing object/array literals triggers infinite loops.
* `useCallback(fn, deps)`: Returns a memoized version of the callback function. Vital when passing functions as props to `React.memo()` children to prevent unnecessary re-renders.
* `useMemo(fn, deps)`: Caches expensive computation results between renders.
* `useRef(initialValue)`: Holds a mutable reference that persists across the full component lifecycle without triggering a re-render upon update.

```jsx
// Clean Responsive Banking Filter Component (Material UI)
import React, { useState, useMemo, useCallback } from 'react';
import { Box, TextField, Table, TableHead, TableRow, TableCell, TableBody, Chip } from '@mui/material';

export const TransactionTable = ({ transactions }) => {
  const [filterText, setFilterText] = useState('');

  // Memoize filtered dataset to prevent expensive re-computations on unrelated renders
  const filteredData = useMemo(() => {
    return transactions.filter(t => 
      t.recipient.toLowerCase().includes(filterText.toLowerCase()) ||
      t.accountNumber.includes(filterText)
    );
  }, [transactions, filterText]);

  const handleFilterChange = useCallback((e) => {
    setFilterText(e.target.value);
  }, []);

  return (
    <Box sx={{ width: '100%', overflowX: 'auto', p: 2 }}>
      <TextField 
        label="Filter by recipient or account" 
        variant="outlined" 
        size="small" 
        value={filterText}
        onChange={handleFilterChange}
        sx={{ mb: 2, minWidth: 280 }}
      />
      <Table size="small">
        <TableHead>
          <TableRow>
            <TableCell>Tx ID</TableCell>
            <TableCell>Recipient</TableCell>
            <TableCell align="right">Amount</TableCell>
            <TableCell align="center">Status</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {filteredData.map(row => (
            <TableRow key={row.id} hover>
              <TableCell>{row.id}</TableCell>
              <TableCell>{row.recipient}</TableCell>
              <TableCell align="right">${row.amount.toFixed(2)}</TableCell>
              <TableCell align="center">
                <Chip 
                  label={row.status} 
                  color={row.status === 'SETTLED' ? 'success' : 'warning'} 
                  size="small" 
                />
              </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </Box>
  );
};
```

---

## 2. Python Concurrency & Backend Internals

### The Global Interpreter Lock (GIL) & Execution Models
* **The GIL**: A mutex that prevents multiple native OS threads from executing Python bytecodes simultaneously in CPython.
* **Concurrency Decision Matrix**:

| Workload Type | Ideal Model | Python Tool | Key Characteristics |
| :--- | :--- | :--- | :--- |
| **I/O-Bound** (Network API calls, DB queries) | Cooperative Multitasking | `asyncio` (`async/await`) | Single OS thread, non-blocking event loop, sub-millisecond context switches, low memory. |
| **I/O-Bound** (Legacy sync blocking libraries) | Preemptive Multi-threading | `threading` / `ThreadPoolExecutor` | Kernel threads, GIL released during socket read/write, higher memory footprint. |
| **CPU-Bound** (Cryptographic signing, matrix math) | Multiprocessing | `multiprocessing` / `ProcessPool` | Bypasses GIL by spawning independent OS processes with separate memory spaces. |

```python
# High-Throughput Async Banking Ingestion Endpoint
import asyncio
from typing import List, Dict

async def fetch_account_balance(account_id: str) -> Dict[str, float]:
    # Simulate non-blocking I/O network call to core banking ledger
    await asyncio.sleep(0.05)
    return {"account_id": account_id, "balance": 15420.50}

async def process_batch_accounts(account_ids: List[str]) -> List[Dict[str, float]]:
    # Run requests concurrently using asyncio.gather
    tasks = [fetch_account_balance(acc_id) for acc_id in account_ids]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    return [r for r in results if not isinstance(r, Exception)]
```

---

## 3. Database Engineering: MongoDB & Document Modeling

### MongoDB vs Traditional Relational SQL
* **Relational (RDBMS)**: Normalized schemas, strict ACID, foreign keys, tables. Ideal for double-entry ledger settlement where schema rigidity is paramount.
* **MongoDB**: Polymorphic JSON-like documents, dynamic schema, horizontal sharding via partition keys, high read/write throughput for unstructured customer profiles and audit feeds.

### Indexing Strategies in MongoDB
1. **Single-Field Index**: `db.transactions.createIndex({ timestamp: -1 })`
2. **Compound Index (ESR Rule - Equality, Sort, Range)**:
   * Example: Searching transactions for a customer within a date range:
   * Query: `find({ accountId: "A123", amount: { $gt: 100 } }).sort({ timestamp: -1 })`
   * Optimal Index: `{ accountId: 1, timestamp: -1, amount: 1 }` (Equality: `accountId`, Sort: `timestamp`, Range: `amount`).
3. **Aggregation Pipeline Example**:
```javascript
// Calculate total debit volume per currency in the last 24 hours
db.transactions.aggregate([
  { 
    $match: { 
      type: "DEBIT", 
      status: "SETTLED", 
      createdAt: { $gte: new Date(Date.now() - 24*60*60*1000) } 
    } 
  },
  { 
    $group: { 
      _id: "$currency", 
      totalVolume: { $sum: "$amount" }, 
      count: { $sum: 1 } 
    } 
  },
  { $sort: { totalVolume: -1 } }
]);
```

---

## 4. Cloud & DevOps: AWS Serverless & Terraform

### AWS Serverless Key Components
1. **AWS Lambda**: Event-driven serverless compute. Cold starts occur when a new micro-VM container is initialized. Mitigated using **Provisioned Concurrency** or keeping bundles small.
2. **Amazon DocumentDB**: Fully managed MongoDB-compatible document database with multi-AZ replication.
3. **Amazon S3 & CloudFront**: S3 stores static artifacts; CloudFront distributes them across global edge locations with sub-20ms latency.

### Terraform Infrastructure as Code (IaC) Essentials
* **Declarative Configuration**: You define the desired end-state, and Terraform determines the execution graph (`terraform plan` $ightarrow$ `terraform apply`).
* **State Management (`terraform.tfstate`)**: Keeps track of provisioned resource IDs. Stored remotely in **Amazon S3 with DynamoDB state locking** to prevent concurrent write collisions.
